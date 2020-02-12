"""
1.员工信息：编号、姓名、工资、性别
2.编号不允许修改，不允许重复
3.功能实现：
3.1新增员工信息
3.2根据员工编号删除员工信息
3.3根据员工编号修改员工信息
3.4显示所有员工信息
3.5退出员工管理系统
"""
employee = {}
# 定义一个全局变量employee_num用于存储总录入的员工记录数
# 也是方便在字典中建字典
global employee_num
employee_num = 0


def menu():
    print('''
        1.新增员工信息
        2.根据员工编号删除员工信息
        3.根据员工编号修改员工信息
        4.显示所有员工信息
        5.退出员工管理系统
    ''')
    return True


# 增加员工信息
def increase():
    global employee_num
    id = input('请输入编号：')
    # 当表中有员工记录时，查询id，重复则不再录入
    if len(employee):
        for key, value in employee.items():
            if value['id'] == id:
                print("该员工编号重复了")
                return False
    name = input('请输入姓名：')
    salary = input('请输入工资：')
    sex = input('请输入性别：')
    employee_info = {}
    # 先为该条员工记录建立一个空字典
    employee[employee_num] = employee_info
    # 为该条员工记录添加关键字和值
    employee_info['id'] = id
    employee_info['name'] = name
    employee_info['salary'] = salary
    employee_info['sex'] = sex
    employee_num += 1
    return True


# 根据id删除员工记录
def del_employee(id):
    # 如果员工记录数为0，则该表不存在
    if not len(employee):
        print("员工数位空！")
        return False
    # 遍历字典（字典中套了一个字典，单个员工的信息存放在外层字典的value中）
    for key, value in employee.items():
        if value.get('id') == id:
            del employee[key]
            return True
    print("不存在此员工！")
    return False


# 根据id修改员工信息
def modify_employee(id):
    if not len(employee):
        print("员工数位空！")
        return False
    for key, value in employee.items():
        if value.get('id') == id:
            name = input('请输入姓名：')
            salary = input('请输入工资：')
            sex = input('请输入性别：')
            value['name'] = name
            value['salary'] = salary
            value['sex'] = sex
            return True
    print("不存在此员工！")
    return False


# 打印总员工信息
def print_employee():
    if len(employee):
        print('编号      姓名      工资      性别')
        print('--------------------------------------------')
        for key, value in employee.items():
            print(value['id'], value['name'], value['salary'], value['sex'])
        return True
    print("暂无员工信息")
    return False


# 主函数
if __name__ == '__main__':
    while 1:
        menu()
        i = input("请输入序号：")
        if i == '1':
            increase()
            continue
        elif i == '2':
            id = input("请输入该员工编号：")
            del_employee(id)
            continue
        elif i == '3':
            id = input("请输入该员工编号：")
            modify_employee(id)
            continue
        elif i == '4':
            print_employee()
            continue
        elif i == '5':
            break
