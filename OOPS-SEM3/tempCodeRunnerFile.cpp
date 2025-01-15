void Operation::display() {
    cout << "The " << k << "th largest element in the array is: " << target << endl;
}

int main() {
    Operation op;
    op.getdata();
    op.klargest();
    op.display();
    return 0;
}

