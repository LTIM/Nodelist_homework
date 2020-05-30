class Node():#链表
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
class linklist():
    def __init__(self):
        self.head = None
    def length(self):#判断链表的长度
        count = 0
        pointer = self.head#将头节点的next指针赋值给head
        while pointer:#判断头节点指针是否为空
            count+=1
            pointer = pointer.next#指向下一个节点
        return count
    def items(self):
        l=[]
        pointer = self.head#将头节点的指针赋给pointer
        while pointer:
            l.append(pointer.data)
            pointer = pointer.next
        if l is not None:
            return l
        else :
            return "list is null"
    def add(self,data):#头插法
       if data is not None:
            node = Node(data)
            node.next=self.head
            self.head=node
            print('add success')
       else:
           print('data can not is null')

    def appand(self,data):#尾插法
        if data is not None:
            node = Node(data)#初始化一个链表节点
            if self.head is not None:#判断是否为空表
                pointer = self.head#初始化一个指针
                while pointer.next is not None:#判断指针是否为空
                    pointer = pointer.next#指针后移
                pointer.next = node#
                print('添加成功')
            else:
                self.head = node
                print('添加成功')
    def insert(self,data,locate):
        if data is not None and locate is not None:
            node  = Node(data)
            if locate<=1:#插入位置在头节点
                node.next = self.head
                self.head = node
            elif locate>(self.length()):#大于长度直接插在队尾
                self.appand(data)
            else:
                pointer = self.head
                for i in range(1,locate-1):
                    pointer = pointer.next
                node.next = pointer.next
                pointer.next = node
        else:
            print('输入错误')
    def delete(self,data):
        if data is not Node:
            pointer = self.head#头节点指针
            per =pointer#指向poinetr的前一个节点 刚开始时指向同一个节点
            s = self.head
            count = 0  # 计数器
            while pointer:
                if pointer.data != data:#判断是否和待删除数据相等
                    per = pointer
                    pointer = pointer.next
                else:
                    per.next = pointer.next#直接将per指向pointer下一个节点 既删除了pointer所指的这个节点
                    pointer = pointer.next
                    count = count +1
            #前面的while循环因为per = pointer这一初始赋值 当头节点为
            if s.data == data:#判断头节点是否为要删除的节点
                self.head=s.next
            return count
        else:
            print('data is null')
    def find(self,data):
        pointer = self.head
        locate=[]#位置信息存在这个list中存储
        count = 1#位置信息计数器
        while pointer:
            if pointer.data == data:
                locate.append(count)#将节点位置存到locate中
                count = count + 1#计数器后移一位
            else:
                count = count+1
            pointer = pointer.next#指针后移
        return locate



if __name__ =='__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(4)
    node4 = Node(5)
    linklist_1 = linklist()
    linklist_1.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    print(linklist_1.length())
    print(linklist_1.items())
    linklist_1.add(4)
    print(linklist_1.items())
    linklist_1.appand(5)
    print(linklist_1.items())
    linklist_1.insert(411,3)
    print(linklist_1.items())
    a = linklist_1.delete(4)
    if a == 0:
        print('data not in nodelist')
    else:
        print(linklist_1.items())
        print(a)
    print(linklist_1.find(5))