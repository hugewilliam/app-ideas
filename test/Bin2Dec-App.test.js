import bin2Dec from '../code/Bin2Dec-App'

test('Bin2Dec method test, input \'100\' than output 4', () => {
  expect(bin2Dec('100')).toBe(4)
})

test('Bin2Dec method test, input \'1011\' than output 11', () => {
  expect(bin2Dec('1011')).toBe(11)
})

test('Bin2Dec method test, input other type', () => {
  expect(bin2Dec(12311)).toBe('type error!')
})


test('Bin2Dec method test, enter over 8 binary digits', () => {
  expect(bin2Dec('101110110')).toBe('stack overflow!')
})

test('Bin2Dec method test, input other than 0 or 1', () => {
  expect(bin2Dec('1234')).toBe('invalid!')
})