import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fund = pd.read_csv('./csv/004616.csv', dtype={'fcode': str})
    fund['date'] = pd.to_datetime(fund['fdate'])
    fund = fund.set_index('fdate').sort_index(ascending=False)
    x = fund.index
    y = fund['NAV']
    plt.plot(x, y)
    plt.show()
