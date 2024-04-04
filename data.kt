private class Node(private val maxChildren: Short) {
    var child1: Node? = null
    var child2: Node? = null
 
    fun canAddChildren(): Boolean {
        var numChildren = 0
        if (child1 != null) numChildren++
        if (child2 != null) numChildren++
        return numChildren < maxChildren
    }
 
    fun children() = listOfNotNull(child1, child2)
 
    fun addChild(child: Node) {
        if (child1 == null) {
            child1 = child
        } else if (child2 == null) {
            child2 = child
        } else {
            throw Exception()
        }
    }
}
 
fun main() {
    val t = readln().toInt()
 
    repeat(t) {
        val input = readln().split(" ").map { it.toInt() }
        val a = input[0]
        val b = input[1]
        val c = input[2]
 
        println(minTreeHeight(a, b, c))
    }
}
 
private fun minTreeHeight(a: Int, b: Int, c: Int): Int {
    if (a + 1 != c) {
        return -1
    }
 
    val nodesToAdd = mutableListOf<Node>().apply {
        addAll(List(a) { Node(maxChildren = 2) })
        addAll(List(b) { Node(maxChildren = 1) })
        addAll(List(c) { Node(maxChildren = 0) })
    }
 
    val root = try {
        createTree(nodesToAdd)
    } catch(e: Exception) {
        return -1
    }
 
    return maxTreeHeight(root)
}
 
private fun createTree(nodesToAdd: List<Node>): Node {
    val count = nodesToAdd.size
    val root = nodesToAdd.first()
    var added = 1
    val queue = ArrayDeque<Node>()
    queue.add(root)
    while (queue.isNotEmpty() && added < count) {
        val parent = queue.removeFirst()
        while (parent.canAddChildren()) {
            val newNode = nodesToAdd[added]
            parent.addChild(newNode)
            added++
        }
        queue.addAll(parent.children())
    }
 
    if (added != count) throw Exception()
 
    return root
}
 
private fun maxTreeHeight(root: Node, countFrom: Int = 0): Int = if (root.children().isNotEmpty()) {
    root.children().maxOf { maxTreeHeight(it, countFrom + 1) }
} else {
    countFrom
}