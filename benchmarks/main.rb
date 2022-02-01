def helloWorld()
  puts "Hello World"
end

def factorial(n)
  if n <= 1
    return 1
  else
    return n * factorial(n - 1)
  end
end

def sum(n)
  s = 0
  for i in 0..n
    s += i
  end
  return s
end

$count = 0

def recurFib(n, start)
  
  if n <= 1
    return n
  else
    #if n % 10 == 0
    #  $count += 1
    #end
    #if $count % 1000000 == 0
      # puts $count
     # elapsed = Time.now - start
      # puts "hit ".concat($count.to_s).concat(" at ").concat(elapsed.to_s)
    #end
    return recurFib(n - 1, start) + recurFib(n - 2, start)
  end
end

def iterFib(n)
  f = 0
  p1 = 0
  p2 = 1
  for i in 0..n+1
    f = p1 + p2
    if i % 2 == 0
      p1 += p2
    else
      p2 += p1
    end
  end
  return f
end

def maxSearch()
  nums = []
  for i in 0..1000000
    nums[i] = rand(1000000)
  end
  maximum = 0
  for i in 0..1000000
    if nums[i] > maximum
      maximum = nums[i]
    end
  end
  return maximum
end

def printTriangle(size)
  for i in (size).downto(1)
    for j in 1..i
      print j.to_s.concat(" ")
    end
    puts "\n"
  end
end

def main()
  inputs = ARGV
  len = inputs.length 
  if(len == 0)
      puts("Invalid usage: ./main.rb <choice>\n");
      puts("Choices:\n");
      puts("[0]: hello\n[1]: fact\n[2]: sum\n[3]: recur_fib\n[4]: iter_fib\n[5]: max\n[6]: triangle\n");
      return
  end
  choice = inputs[0].to_i
  if(choice > 6 or choice < 0)
    puts("Invalid choice: " + choice.to_s)
    return
  end

  start = Time.now

  if choice == 0
    helloWorld()
  elsif choice == 1
    puts factorial(20)
  elsif choice == 2
    puts sum(1000000)
  elsif choice == 3
    puts recurFib(50, 1)
  elsif choice == 4
    puts iterFib(50)
  elsif choice == 5
    puts maxSearch()
  elsif choice == 6
    printTriangle(100)
  end

  elapsed = Time.now - start
  puts elapsed
end

main()
