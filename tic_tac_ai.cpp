#include <iostream>
using namespace std; 
void initializeBoard(char board[3][3]);
void displayBoard(const char board[3][3]);
bool checkWin(const char board[3][3], char player);
bool isFull(const char board[3][3]);
void makeMove(char board[3][3], char player);
void aiMove(char board[3][3]);

int main() {
    char board[3][3];
    char currentPlayer = 'X';
    bool winner = false;

    initializeBoard(board);

    while (!winner && !isFull(board)) {
        displayBoard(board);
        
        if (currentPlayer == 'X') {
            makeMove(board, currentPlayer);
        } else {
            aiMove(board);
        }

        winner = checkWin(board, currentPlayer);
        if (winner) {
            displayBoard(board);
            cout << "Player " << currentPlayer << " wins!" << endl;
            break;
        }

        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X'; 
    }

    if (!winner) {
        displayBoard(board);
        cout << "It's a draw!" << endl;
    }

    return 0;
}

void initializeBoard(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}

void displayBoard(const char board[3][3]) {
    cout << "\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << " " << board[i][j] << " ";
            if (j < 2) cout << "|";
        }
        cout << "\n";
        if (i < 2) cout << "---|---|---\n";
    }
    cout << "\n";
}

bool checkWin(const char board[3][3], char player) {
    for (int i = 0; i < 3; i++) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
            (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
            return true;
        }
    }

    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
        (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
        return true;
    }

    return false;
}

bool isFull(const char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') {
                return false;
            }
        }
    }
    return true;
}

void makeMove(char board[3][3], char player) {
    int row, col;
    cout << "Player " << player << ", enter your move (row and column): ";
    cin >> row >> col;

    while (row < 1 || row > 3 || col < 1 || col > 3 || board[row - 1][col - 1] != ' ') {
        cout << "Invalid move. Try again: ";
        cin >> row >> col;
    }

    board[row - 1][col - 1] = player;
}

void aiMove(char board[3][3]) {
    int bestRow = -1, bestCol = -1;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') {
             
                board[i][j] = 'O';
                if (checkWin(board, 'O')) {
                    return; 
                }
                board[i][j] = 'X';
                if (checkWin(board, 'X')) {
                    board[i][j] = 'O'; 
                    return;
                }
                board[i][j] = ' '; 
            }
        }
    }

    for (int i = 0; i < 3 && bestRow == -1; i++) {
        for (int j = 0; j < 3 && bestCol == -1; j++) {
            if (board[i][j] == ' ') {
                bestRow = i;
                bestCol = j;
            }
        }
    }

    if (bestRow != -1 && bestCol != -1) {
        board[bestRow][bestCol] = 'O';
    }
}
