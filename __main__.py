from functions import *

def main():
    print('=' * 30)
    print('RUNNING ANALYZER'.center(30))
    print('=' * 30)
    hist = hist_run()
    data_analysis(hist)
    goal_dist(hist)

if __name__ == '__main__':
    main()