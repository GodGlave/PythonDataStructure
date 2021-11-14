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