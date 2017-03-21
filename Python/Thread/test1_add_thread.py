# utf-8
# python3.5

import threading as td

def thread_job():
    print("This is added thread, number is %s" %td.current_thread())


def main():
    added_thread = td.Thread(target=thread_job)
    added_thread.start()
    # print(td.active_count())
    # print(td.enumerate())
    # print(td.current_thread())

if __name__ == '__main__':
    main()
