function find_max {
    let max_num = Number.NEGATIVE_INFINITY
    for (let num of nums) {
        if (num >max_num) {
            max_num = num
        }
    }
    return max_num
}