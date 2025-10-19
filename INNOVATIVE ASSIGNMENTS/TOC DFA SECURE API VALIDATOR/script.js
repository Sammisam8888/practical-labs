/*
 * script.js
 *
 * This file contains the client‑side logic for the API Route Security
 * Analyzer.  When the user submits the form we gather the endpoint,
 * HTTP method and optional body then build a deterministic finite
 * automaton (DFA) representing a sequence of security checks.  We
 * derive recommended best practices based on industry guidance from
 * sources like OWASP and Frontegg (see report for citations).  The
 * resulting diagram, table and recommendations are rendered into the
 * DOM.
 */

// Wait for the DOM to be fully loaded before attaching listeners.
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("apiForm");
  const resultSection = document.getElementById("result");
  const analysisOutput = document.getElementById("analysisOutput");
  const diagramArea = document.getElementById("diagramArea");
  const stateTable = document.getElementById("stateTable");

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    // Fetch user inputs
    const path = document.getElementById("path").value.trim();
    const method = document.getElementById("method").value.trim().toUpperCase();
    const body = document.getElementById("body").value.trim();

    // Perform analysis and update the UI
    const analysis = analyzeAPI(path, method, body);
    renderAnalysis(analysis, analysisOutput, diagramArea, stateTable);
    resultSection.classList.remove("hidden");
  });
});

/**
 * Build a DFA model and security recommendations for a given API endpoint.
 *
 * @param {string} path - The relative URL path of the API endpoint
 * @param {string} method - The HTTP method (e.g. GET, POST, etc.)
 * @param {string} body - Sample request payload (may be empty)
 * @returns {object} An object containing states, transitions and suggestions
 */
function analyzeAPI(path, method, body) {
  // Basic checks on the HTTP method
  const allowedMethods = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"];
  const methodIsValid = allowedMethods.includes(method);

  // Determine if the endpoint uses path parameters (e.g. /users/{id} or :id)
  const pathParamRegex = /\{[^\}]+\}|:[^/]+/g;
  const hasPathParams = pathParamRegex.test(path);

  // Determine if the endpoint includes query parameters (e.g. /search?q=foo)
  const hasQueryParams = path.includes("?");

  // Determine if a request body was supplied (common for POST, PUT, PATCH)
  const hasBody = body.length > 0;

  // Build a list of human friendly security recommendations based on
  // recognized best practices.  These recommendations are drawn from
  // authoritative sources like OWASP and Frontegg which stress
  // measures such as HTTPS, strong authentication, input validation,
  // rate limiting and regular patching【254863355684197†L160-L190】
  //【254863355684197†L204-L214】.
  const recommendations = [];
  recommendations.push(
    "Use HTTPS/TLS for secure communication to prevent data interception and tampering."
  );
  recommendations.push(
    "Implement strong authentication and authorization. Prefer OAuth 2.0 or OpenID Connect with signed tokens to verify client identity and control access【254863355684197†L160-L190】."
  );
  recommendations.push(
    "Validate and sanitize all inputs—including path parameters, query strings and JSON bodies—to prevent injection attacks and excessive data exposure【254863355684197†L160-L176】."
  );
  recommendations.push(
    "Enforce rate limiting and throttling to protect against denial‑of‑service attacks and abuse【254863355684197†L242-L247】."
  );
  recommendations.push(
    "Regularly update dependencies and conduct security testing to address newly discovered vulnerabilities【254863355684197†L204-L214】."
  );
  if (["POST", "PUT", "PATCH", "DELETE"].includes(method)) {
    recommendations.push(
      "For state‑changing requests (" +
        method +
        "), employ CSRF protection, idempotency keys and ensure only authorized users can modify resources."
    );
  }
  if (!methodIsValid) {
    recommendations.push(
      "The HTTP method appears to be non‑standard. Restrict endpoints to valid methods such as GET, POST, PUT, PATCH or DELETE."
    );
  }
  if (hasPathParams) {
    recommendations.push(
      "Your path contains dynamic parameters. Validate and authorize access to each resource identifier to prevent Broken Object Level Authorization【947172881642444†L55-L67】."
    );
  }
  if (hasQueryParams) {
    recommendations.push(
      "The endpoint uses query parameters. Validate and encode query inputs and avoid placing sensitive data in the URL."
    );
  }
  if (hasBody) {
    recommendations.push(
      "A JSON body is supplied. Validate the JSON schema, enforce content‑type headers and limit payload size to prevent injection and resource exhaustion." 
    );
  }

  // Define the core states of the DFA.  Each state is represented by an
  // identifier and a display label.  The order here determines the
  // conceptual flow of the security checks.
  const states = [
    { id: "Start", label: "Start" },
    { id: "CheckMethod", label: "Validate HTTP Method" },
    { id: "CheckHTTPS", label: "Validate HTTPS" },
    { id: "Authenticate", label: "Authenticate Request" },
    { id: "Authorize", label: "Authorize User" },
    { id: "ValidateInput", label: "Validate & Sanitize Input" },
    { id: "RateLimit", label: "Enforce Rate Limit" },
    { id: "Respond", label: "Generate Response" },
    { id: "Error", label: "Error / Reject" }
  ];

  // Build the transitions for the DFA.  Each transition describes a
  // condition under which the system moves from one state to another.
  const transitions = [];
  transitions.push({ from: "Start", to: "CheckMethod", condition: "API call received" });
  transitions.push({ from: "CheckMethod", to: "CheckHTTPS", condition: "Valid method" });
  transitions.push({ from: "CheckMethod", to: "Error", condition: "Invalid method" });
  transitions.push({ from: "CheckHTTPS", to: "Authenticate", condition: "HTTPS used" });
  transitions.push({ from: "CheckHTTPS", to: "Error", condition: "Not HTTPS" });
  transitions.push({ from: "Authenticate", to: "Authorize", condition: "Token valid" });
  transitions.push({ from: "Authenticate", to: "Error", condition: "Missing/invalid token" });
  transitions.push({ from: "Authorize", to: "ValidateInput", condition: "Access permitted" });
  transitions.push({ from: "Authorize", to: "Error", condition: "Access denied" });
  transitions.push({ from: "ValidateInput", to: "RateLimit", condition: "Input valid" });
  transitions.push({ from: "ValidateInput", to: "Error", condition: "Invalid input" });
  transitions.push({ from: "RateLimit", to: "Respond", condition: "Within limit" });
  transitions.push({ from: "RateLimit", to: "Error", condition: "Rate limit exceeded" });
  transitions.push({ from: "Respond", to: "Respond", condition: "" }); // self loop indicating end

  return {
    recommendations,
    states,
    transitions,
    methodIsValid,
    hasPathParams,
    hasQueryParams,
    hasBody
  };
}

/**
 * Render the analysis results to the page.  This function populates the
 * recommendations list, generates a Mermaid diagram and constructs a
 * state table from the provided DFA model.
 *
 * @param {object} analysis The result of analyzeAPI()
 * @param {HTMLElement} analysisOutput Container for recommendations
 * @param {HTMLElement} diagramArea Container where the diagram will be rendered
 * @param {HTMLElement} tableEl Table element for the state table
 */
function renderAnalysis(analysis, analysisOutput, diagramArea, tableEl) {
  // Clear previous content
  analysisOutput.innerHTML = "";
  diagramArea.innerHTML = "";
  tableEl.innerHTML = "";

  // Render recommendations as a bulleted list
  const list = document.createElement("ul");
  analysis.recommendations.forEach((rec) => {
    const li = document.createElement("li");
    li.textContent = rec;
    list.appendChild(li);
  });
  analysisOutput.appendChild(list);

  // Build a mermaid diagram definition string from the transitions
  let diagram = "stateDiagram-v2\n";
  // Mark the initial state
  diagram += "    [*] --> Start\n";
  // Iterate through each transition and append to the diagram
  analysis.transitions.forEach((t) => {
    // Escape colon in labels (Mermaid uses colon as syntax delimiter)
    const label = t.condition ? `: ${t.condition.replace(/:/g, '\\:')}` : "";
    diagram += `    ${t.from} --> ${t.to}${label}\n`;
  });
  // Indicate termination by returning to final state
  diagram += "    Respond --> [*]\n";

  // Insert diagram into the page
  const pre = document.createElement("pre");
  pre.className = "mermaid";
  pre.textContent = diagram;
  diagramArea.appendChild(pre);
  // Use mermaid to render the diagram.  Because mermaid.initialize() was
  // called in index.html we can now call run to render diagrams in the
  // provided container.
  if (window.mermaid) {
    window.mermaid.run({ querySelector: "#diagramArea .mermaid" });
  }

  // Build state table header
  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");
  ["Current State", "Condition/Event", "Next State"].forEach((text) => {
    const th = document.createElement("th");
    th.textContent = text;
    headerRow.appendChild(th);
  });
  thead.appendChild(headerRow);
  tableEl.appendChild(thead);

  // Build table body
  const tbody = document.createElement("tbody");
  analysis.transitions.forEach((t) => {
    const tr = document.createElement("tr");
    const tdFrom = document.createElement("td");
    const tdCond = document.createElement("td");
    const tdTo = document.createElement("td");
    tdFrom.textContent = t.from;
    tdCond.textContent = t.condition || "—";
    tdTo.textContent = t.to;
    tr.appendChild(tdFrom);
    tr.appendChild(tdCond);
    tr.appendChild(tdTo);
    tbody.appendChild(tr);
  });
  tableEl.appendChild(tbody);
}