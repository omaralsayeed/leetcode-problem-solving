/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
    numberOfAbsents = s.split("A").length - 1
    numberOfLatenessMoreThanThree = s.split("LLL").length - 1
    return numberOfAbsents < 2 && numberOfLatenessMoreThanThree < 1
};