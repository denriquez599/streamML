from regression import Regression


def main():
    mse = Regression.linear_regression()
    print('mse:', mse)


if __name__ == "__main__":
    main()