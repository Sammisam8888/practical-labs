#include<iostream>
#include <ctime>
using namespace std;

class Sort {
    int *arr,n;
    int arrsize[4]={5,10,15,20};
	double timediff[48];
	string sortingtype[4]={"Selection Sort ","Insertion Sort ","Bubble Sort ","Heap Sort "};
	void SelectionSort(){		
	}
	void InsertionSort(){
	}
	void BubbleSort(){
	}
    void HeapSort(){
    }

    void display(string message = "") {
        if (!message.empty()) {
            cout << message << endl;
        }
        cout << "The elements of the array are: ";
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    void getdata() {
		cout<<"Enter "<<n<<" elements for the array : ";
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
	}

    void comparetime(string minType, double minTime, string maxType, double maxTime) {
		cout << "The case with the minimum time: " << minType << " took " << minTime << " seconds" << endl;
        cout << "The case with the maximum time: " << maxType << " took " << maxTime << " seconds" << endl;
    }	

public:
    void runsort() {
        string mintype, maxtype;
        for (int i = 0; i < 4; i++) {
        double mintime = 1e9, maxtime = 0;
            n=arrsize[i];
            getdata();
			for (int j=0;j<4;j++){
            timediff[i*j*3] = double(clock())/CLOCKS_PER_SEC;
			cout<<"For ";
			switch(j){
			case 0:
				SelectionSort();
				break;
			case 1:
				InsertionSort();
				break;
			case 2:
				BubbleSort();
				break;
			case 3:
				HeapSort();
				break;
			}
			
			timediff[i*3*j+1]=double(clock()) / CLOCKS_PER_SEC;
			timediff[i*3*j+2] = timediff[i*3*j+1] - timediff[i*j*3];
            cout<<"For "<<sortingtype[j]<<endl;
            cout << "Start Time: " <<  timediff[i*j*3]  << " seconds" << endl;
            cout << "End Time: " << timediff[i*3*j+1] << " seconds" << endl;
            cout << "Time taken: " << timediff[i*3*j+2] << " seconds" << endl;
            if (timediff[i*3*j+2] < mintime) {
                mintime = timediff[i*3*j+2];
				mintype= sortingtype[j];
            }
            if (timediff[i*3*j+2] > maxtime) {
                maxtime = timediff[i*3*j+2];
                maxtype = sortingtype[j];
            }
		}

            delete[] arr;
			comparetime(mintype, mintime, maxtype, maxtime);
        }

    }
};

int main() {
    Sort s;
    s.runsort();
    return 0;
}
