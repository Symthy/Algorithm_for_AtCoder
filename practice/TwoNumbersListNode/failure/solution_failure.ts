type ReturnObj = { node: ListNode, upNum: number }

function multiplyTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  if (l1.val === 0 && l2.val === 0) {
      return new ListNode(0, null);
  }

  const retObj = multiplyNodeValue(l1, l2);
  if (retObj.upNum > 0) {
      return new ListNode(retObj.upNum, retObj.node);
  }
  return retObj.node;
};

function multiplyNodeValue(listNode1: ListNode | null, listNode2: ListNode | null): ReturnObj {
  if (listNode1.next == null && listNode2.next == null) {
    return { node: new ListNode(), upNum: 0 };
  }
  const retObj = multiplyNodeValue(listNode1.next, listNode2.next);
  const num = listNode1.val * listNode2.val + retObj.node.val;
  const firstPlaceNum = num % 10;
  const tenthPlaceNum = (num - firstPlaceNum) / 10;

  retObj.node.val = firstPlaceNum;
  const beforeNode = new ListNode();
  beforeNode.next = retObj.node;

  return { node: beforeNode, upNum: tenthPlaceNum };
}
