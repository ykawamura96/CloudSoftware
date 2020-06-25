from collections import namedtuple

MeasuredData = namedtuple('MeasuredData',
                          ['os', 'title', 'x_data', 'y_data', 'x_label', 'y_label'])


if __name__ == "__main__":
    "curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -"
