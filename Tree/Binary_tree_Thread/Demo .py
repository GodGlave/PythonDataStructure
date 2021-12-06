#遍历中序线索二叉树非递归
def InOrderTraverse_thr(T):
    # TreeNode就是树的根结点
    TreeNode = T.lchild
    while TreeNode is not T:
        while TreeNode.ltag == 0:
            # 找到了树最左边的那个结点(不一定是叶结点)
            TreeNode = TreeNode.lchild
        print(TreeNode.data,end=',')
        while TreeNode.rchild is not T and TreeNode.rtag == 1:
            # 线索后继，沿右线索访问后继节点
            TreeNode = TreeNode.rchild
            print(TreeNode.data,end=',')
        # rtag=0就开始寻找右子树最左边那个结点
        TreeNode = TreeNode.rchild


#线索二叉树生成过程
def InThread(TreeNode):
    if TreeNode is not None:
        # 递归, 线索化左子树
        InThread(TreeNode.lchild)
        if TreeNode.lchild is None:
            # 当前结点没有左孩子
            # 将当前结点的ltag置为1, 表示lchild域指向的是前驱
            TreeNode.ltag = 1
            TreeNode.lchild = PreNode
        if PreNode.rchild is None:
            # 前驱结点没有右孩子
            # 将前驱结点的rtag置为1, 表示rchild域指向的是后继, 即当前的TreeNode
            PreNode.rtag = 1
            PreNode.rchild = TreeNode
        # 标记刚刚访问的结点为下个结点的前驱结点
        PreNode = TreeNode
        InThread(TreeNode.rchild)