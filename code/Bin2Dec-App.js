/* Projects/1-Beginner/Bin2Dec-App.md */

export default function bin2Dec(bin) {
  if (typeof bin !== 'string') return 'type error!'
  if (!/^[0-1]+$/.test(bin)) return 'invalid!'
  const length = bin.length
  if (length > 8) return 'stack overflow!'

  // let decimal = 0
  // for (let i = 0; i < length; i++) {
  //   const current = bin[length - i - 1] * 2 ** i
  //   decimal += current
  // }
  // return decimal

  return bin.split('').reverse().reduce((decimal, b, i) => decimal += b * 2 ** i, 0)
}