def eingabe()
    puts "Gib eine Liste von Zahlen ein, getrennt durch Leerzeichen:"
    input = gets.chomp
    zahlen = input.split.map { |zahl| zahl.to_f }
    return zahlen
  end
  
  def durchschnitt(zahlen)
    summe = zahlen.reduce(:+)
    durchschnitt = summe / zahlen.length
    return durchschnitt
  end
  
  zahlen = eingabe()
  ergebnis = durchschnitt(zahlen)
  puts "Der Durchschnitt der eingegebenen Zahlen ist: #{ergebnis}"  