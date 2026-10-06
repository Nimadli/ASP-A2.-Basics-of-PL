#include <iostream>
#include <vector>
#include <chrono>
#include <random>

using namespace std;
using Matrix = vector<vector<double>>;

Matrix MatrixMul(const Matrix& A, const Matrix& B) {
    int rowA = A.size();
    int colA = A[0].size();
    int rowB = B.size();
    int colB = B[0].size();

    if (colA != rowB) throw invalid_argument("Dimension mismatch!");

    Matrix C(rowA, vector<double>(colB, 0.0));

    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colB; j++) {
            for (int k = 0; k < colA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return C;
}

Matrix createRandomMatrix(int rows, int cols) {
    Matrix mat(rows, vector<double>(cols));
    mt19937 gen(0);
    uniform_real_distribution<double> dist(0.0, 1.0);

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            mat[i][j] = dist(gen);
        }
    }
    return mat;
}

int main() {
    int N, M, K;
    cout << "Input matrix dimensions N, M, K: \n";
    cin >> N >> M >> K;

    Matrix A = createRandomMatrix(N, M);
    Matrix B = createRandomMatrix(M, K);

    auto start = chrono::high_resolution_clock::now();

    Matrix C = MatrixMul(A, B);

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;

    cout << duration.count() << " seconds for " << N << 'x' << M << " and " << M << 'x' << K << " matrices\n";

    // Unit test
    A = {{1, 2, 3}, {4, 5, 6}};
    B = {{5, 6}, {3, 4}, {1, 2}};

    start = chrono::high_resolution_clock::now();

    C = MatrixMul(A, B);

    end = chrono::high_resolution_clock::now();
    duration = end - start;

    for (int i = 0; i < C.size(); ++i) {
        for (int j = 0; j < C[0].size(); ++j) {
            cout << C[i][j] << ' ';
        }
        cout << '\n';
    }

    cout << duration.count() << " seconds for small matrices\n";
    return 0;
}