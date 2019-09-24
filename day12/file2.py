def main():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='UTF-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了位未知的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()
