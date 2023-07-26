
//function for mapping a range of numbers to another range of numbers
const scale = (num, in_min, in_max, out_min, out_max) => {
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

'https://css-tricks.com/of-course-we-can-make-a-css-only-clock-that-tells-the-current-time/'