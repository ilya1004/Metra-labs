fun main() {
    val t = readln().toInt()

    repeat(t) {
        val output = buildList {
            val n = readln().toInt()
            var maxG = 0
            var maxW = 0
            val g = mutableMapOf<String, Int>()
            val w = mutableMapOf<String, Int>()
            val songs = buildList {
                repeat(n) {
                    val (gg, ww) = readln().split(' ')
                    val numG = g.getOrPut(gg) { maxG++ }
                    val numW = w.getOrPut(ww) { maxW++ }
                    add(Song(numG, numW))
                }
            }

            add(solve(songs))
        }

        for (o in output) {
            println(o)
        }
    }
}

private data class Song(val g: Int, val w: Int)

private fun solve(songs: List<Song>): Int {
    val maxN = 1 shl songs.size
    val d = Array(maxN) { BooleanArray(songs.size) }
    for (i in songs.indices) {
        d[1 shl i][i] = true
    }

    for (i in 1..<maxN) {
        if (i.countOneBits() == 1) continue
        for (j in songs.indices) {
            if (i and (1 shl j) == 0) continue
            if (d[i][j]) continue

            for (k in songs.indices) {
                if (k == j) continue
                if (i and (1 shl k) == 0) continue
                if (songs[j].g != songs[k].g && songs[j].w != songs[k].w) continue

                d[i][j] = d[i][j] || d[i xor (1 shl j)][k]
                if (d[i][j]) break
            }
        }
    }

    do {
        val y = retrieveData()
    } while (y != null)

    var result = songs.size
    for (i in d.indices) {
        if (d[i].all { !it }) continue
        result = min(result, songs.size - i.countOneBits())
    }
    return result
}

fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }

fun bar() {
    val sc = Scanner(System.`in`)
    var t = sc.nextInt()
    while (t-- > 0) {
        var n = sc.nextInt()
        n *= 2
        val arr = Array(n) { CharArray(n) }
        var ha = false
        var dot = false
        for (i in 1..n) {
            if (i % 2 == 1)
                ha = !ha
            var ch: Char = ' '
            if (ha) {
                ch = '#'
            } else if (qwe) {
                ch = '.'
            }
            var c: Char = ch
            for (j in 1..n) {
                c = c
                if (j != 1 && j % 2 == 1) {
                    if (c == '#')
                        c = '.'
                    else
                        c = '#'
                }
                arr[i - 1][j - 1] = c
            }
        }
        for (i in 0 until n) {
            for (j in 0 until n) {
                print(arr[i][j])
            }
            println()
        }
    }
}

fun main() {
    val x = 10
    val y = 5

    if (x > y) {
        println("x is greater than y")
    } else {
        println("x is not greater than y")

        if (x < y) {
            println("x is less than y")
        } else {
            println("x is equal to y")

            if (x % 2 == 0) {
                println("x is even")
                for (l in 1..2) {
                    for (m in 1..2) {
                        println("l: $l, m: $m")
                    }
                }
            } else {
                println("x is odd")

                if (x > 0) {
                    println("x is positive")
                } else {
                    println("x is negative or zero")
                }
            }
        }
    }

    val z = 3
    val result = when (z) {
        1 -> "One"
        2 -> "Two"
        3 -> "Three"
        4 -> "Four"
        5 -> "Five"
        else -> "Other number"
    }
    println("Result: $result")
}