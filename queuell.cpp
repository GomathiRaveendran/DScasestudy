#include <iostream>
#include<string>
#include <sstream>
#include <vector>
#include <iterator>
using namespace std;

template<class E>
class QueueLL {
private:
	
	E *queue;
	
	class Node
	{
		public:
			Node *next;
			E element;
			
			Node(E elt)
			{
				element = elt;
				next = NULL;
			}
	};
	Node *head;
	Node *tail;
	int sz;
	
public:
	QueueLL(){
		head = NULL;
		tail = NULL;
		sz = 0;
	}
	int size(){
		return sz;
	}

	bool isEmpty(){
		return (sz==0);
	}

	void enqueue(E elt){
		Node *t = new Node(elt);
		if(sz==0)
		{
			head = t;
			tail = t;
			sz++;
			return;
		}
		
		tail->next = t;
		tail = t;
		sz++;
	}

	E dequeue(){
		if(sz==0)
	    {
	    cout<<"Queue Empty Exception"<<endl<<"None"<<endl;
	    return -1;
	    }
	   E x;
	    
	    if(sz==1)
	    {
	    x = head -> element;
	    head = NULL;
	    tail = NULL;
	    sz--;
	    cout<<x<<endl;
	    return x;
	    
	    }
		x = head -> element;
	   	head = head -> next;
	   	sz--;	
	   	cout<<x<<endl;
	   	return x;
    
	}

	E first(){
		return head -> element;
	}
	void displayQueue(){
		if (isEmpty()){
			cout<< "Queue Empty"<<endl;
		}
		else{
			
			Node *t = head;
			while(t!=NULL)
			{
				cout<<t->element<<" ";
				t = t -> next;
			}
			cout << endl;
			return;
		}
	}
};

void getInput(string const &inputStr,vector<string> &myOutput)
{
    stringstream ss(inputStr);
    string st ="";
    while (getline(ss, st, ' ')) {
        myOutput.push_back(st);
    }
}
char trim(string str) 
{ 
   return str[0];
} 

int main(){
	QueueLL<int> queue;
 	string noOfInputs,str;
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    vector<string> myOutput;
 		str="";
 	    getline(cin, str); 
 	    getInput(str,myOutput);
 	    auto it = myOutput.begin();
        //Note:if there is a sequence expected beyond first char, then DO NOT use trim()
 	    if(it[0] == "E"){
 	    	++it;
 	    	queue.enqueue(stoi(*it));
 	        queue.displayQueue();
 	    }
 	    else if(trim(it[0]) == 'D'){
 	    	queue.dequeue();
 	        queue.displayQueue();
 	    }
 	    else if(trim(it[0]) == 'S'){
 	    	cout<<queue.size()<<endl;
 	    }
 	    else if(trim(it[0]) == 'F'){
 	    	cout<<queue.first()<<endl;
 	    }
 	    else if(trim(it[0]) == 'I'){
 	    	if(queue.isEmpty()){
 	    	    cout<<"True"<<endl;
 	    	}
 	    	else{
 	    	    cout<<"False"<<endl;
 	    	}
 	    }
 	    else{
 	        cout<<"Invalid Input"<<endl;
 	    }
 	}
}


