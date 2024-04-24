#include <iostream>
#include <stack>
#include <queue>

using namespace std;

// Node structure for the tree
struct Node {
    int data;
    Node *left, *right;

    Node(int value) : data(value), left(NULL), right(NULL) {}
};

// Function to create a new node
Node* createNode(int value) {
    return new Node(value);
}

// Function to construct the tree based on user input
Node* constructTree() {
    int data;
    cout << "Enter root node value (-1 to stop): ";
    cin >> data;
    if (data == -1)
        return NULL;

    Node* root = createNode(data);

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();

        int leftData, rightData;
        cout << "Enter left child value of " << current->data << " (-1 for no left child): ";
        cin >> leftData;
        if (leftData != -1) {
            current->left = createNode(leftData);
            q.push(current->left);
        }

        cout << "Enter right child value of " << current->data << " (-1 for no right child): ";
        cin >> rightData;
        if (rightData != -1) {
            current->right = createNode(rightData);
            q.push(current->right);
        }
    }

    return root;
}

// Function to perform Depth First Search (DFS) using a stack
void stackDFS(Node* root) {
    if (root == NULL)
        return;

    stack<Node*> s;
    s.push(root);

    while (!s.empty()) {
        Node* current = s.top();
        s.pop();
        cout << current->data << " ";

        if (current->right != NULL)
            s.push(current->right);

        if (current->left != NULL)
            s.push(current->left);
    }
}

int main() {
    // Construct the tree
    Node* root = constructTree();

    // Perform DFS using stack
    cout << "Depth First Search (DFS): ";
    stackDFS(root);
    cout << endl;

    return 0;
}
