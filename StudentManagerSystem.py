#!/opt/homebrew/bin/python3.9
# student_info = []
student_info = [{'id': 1, 'name': 'wj', 'tel': 110}, {'id': 2, 'name': 'lee', 'tel': 120}]


def add_student():
    """添加学员，循环中的i相当于字典名"""
    student_id = int(input('请输入学号: '))
    student_name = input('请输入姓名：')
    student_number = int(input('请输入电话号码：'))
    for i in student_info:
        if student_name == i['name']:
            print('该学生信息已存在！')
            return
    student_dict = {'id': student_id, 'name': student_name, 'tel': student_number}
    student_info.append(student_dict)
    print(student_info)


def del_student():
    """循环列表中字典，若字典中的name与输入的学生姓名一致则删除列表"""
    student_name = input('请输入要删除的学生姓名：')
    for i in student_info:
        if student_name == i['name']:
            del i
            print('已删除！')
            break
        else:
            print('不存在该学员')


def modify():
    student_name = input('请输入要修改的学生姓名：')
    for i in student_info:
        if student_name == i['name']:
            i['tel'] = input('请输入要修改的手机号:')
            return
    print('学生信息不存在！')


def select_student():
    student_name = input('请输入要查询的学生姓名：')
    for i in student_info:
        if student_name == i['name']:
            print(i)
            break
    print('找不到该学员信息')


def show_all():
    for i in student_info:
        print(f"{i['id']}")


def QUIT():
    print('退出系统')
    exit()


def welcome():
    print('欢迎进入学员系统功能如下:\n'
          '1.添加学员\n'
          '2.删除学员\n'
          '3.修改学员信息\n'
          '4.查询学员信息\n'
          '5.显示所有学员信息\n'
          '6.退出系统\n')


while True:
    welcome()
    choice = int(input('请输入：'))
    if choice == 1:
        add_student()
    elif choice == 2:
        del_student()
    elif choice == 3:
        modify()
    elif choice == 4:
        select_student()
    elif choice == 5:
        show_all()
    elif choice == 6:
        QUIT()
