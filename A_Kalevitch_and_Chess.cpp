#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    // Optimize standard I/O operations for performance
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> board(8);
    int black_rows = 0;
    int black_cols = 0;

    // Read the 8x8 chessboard
    for (int i = 0; i < 8; ++i) {
        cin >> board[i];
    }

    // Count how many rows are completely black ('B')
    for (int i = 0; i < 8; ++i) {
        bool all_black = true;
        for (int j = 0; j < 8; ++j) {
            if (board[i][j] != 'B') {
                all_black = false;
                break;
            }
        }
        if (all_black) {
            black_rows++;
        }
    }

    // Count how many columns are completely black ('B')
    for (int j = 0; j < 8; ++j) {
        bool all_black = true;
        for (int i = 0; i < 8; ++i) {
            if (board[i][j] != 'B') {
                all_black = false;
                break;
            }
        }
        if (all_black) {
            black_cols++;
        }
    }

    // Edge Case: If the entire board is black, 8 row strokes (or 8 col strokes) 
    // would color it completely. Otherwise, it's the sum of full rows and columns.
    if (black_rows == 8) {
        cout << 8 << "\n";
    } else {
        cout << black_rows + black_cols << "\n";
    }

    return 0;
}
