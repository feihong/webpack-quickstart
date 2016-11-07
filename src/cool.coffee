require('./cool.styl')

for i in [1..10]
  p = $('<p class=number>').text(i)
  p.appendTo(document.body)
