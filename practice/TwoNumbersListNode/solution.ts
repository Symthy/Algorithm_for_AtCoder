function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  return plusNodeValue(l1, l2);
};

function plusNodeValue(listNode1: ListNode | null, listNode2: ListNode | null,
  upNum: number = 0): ListNode | null {

  if (listNode1 == null && listNode2 == null && upNum === 0) {
    return null;
  }
  const val1 = listNode1 == null ? 0 : listNode1.val;
  const val2 = listNode2 == null ? 0 : listNode2.val;
  const num = val1 + val2 + upNum;
  const firstPlaceNum = num % 10;
  const tenthPlaceNum = (num - firstPlaceNum) / 10;

  const node = new ListNode(
    firstPlaceNum,
    plusNodeValue(
      listNode1 == null ? null : listNode1.next,
      listNode2 == null ? null : listNode2.next,
      tenthPlaceNum)
  );
  return node;
}
