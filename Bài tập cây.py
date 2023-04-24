# Khởi tạo lớp Node gồm các thuộc tính là value và children
class Node:
    def __init__(self, value=None, children=None):
        self.value = value # value là giá trị của nút
        # children là một danh sách chứa các nút con
        # Nếu tham số truyền vào children không rỗng thì gán self.children cho children
        if children is not None:
            self.children = children
        # Ngược lại nếu children rỗng thì sẽ được gán bằng danh sách rỗng
        else:
            self.children = []

# Hàm tạo cây
def build_tree(node_list):
    # Kiểm tra node_list có rỗng không nếu đúng trả về None
    if not node_list:
        return None
    # ngược lại thì hàm khởi tạo một từ điển rỗng nodes để lưu trữ các đối tượng Node và duyệt qua danh sách node_list
    nodes = {}
    for node in node_list:
        # Đối với mỗi nút trong danh sách node_list, chúng ta sẽ tạo một đối tượng Node với giá trị là phần tử đầu tiên trong danh sách node và lưu trữ nó trong từ điển nodes, với node[0] được dùng làm khóa của từ điển.  
        nodes[node[0]] = Node(node[0])
    for node in node_list:
        # Nếu một nút trong danh sách có độ dài lớn hơn 1 chúng ta sẽ lặp qua danh sách các nút con và thêm chúng vào danh sách children
        if len(node) > 1:
            for child in node[1:]:
                nodes[node[0]].children.append(nodes[child])
    # trả về nút gốc của cây
    return nodes[node_list[0][0]]

node_list = [3,4,1,9],[4,5],[5,8,6],[1],[9,2,7]

# Kết quả hiển thị sẽ là : 
#        3
#      / | \
#     4  1  9
#    /     / \
#   5     2   7
#  / \
# 8   6
