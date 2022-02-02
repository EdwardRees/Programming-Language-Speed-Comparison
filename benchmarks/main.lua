function helloWorld()
  print('Hello World')
end

function factorial(n)
  if n < 1 then
    return 1
  else 
    return n * factorial(n - 1)
  end
end

function sum(n)
  local s = 0
  for i=0, n, 1 do
    s = s + i
  end
  return s
end

count = 0

function recurFib(n)
  if n <= 1 then
    return 1
  else
    return recurFib(n - 1) + recurFib(n - 2)
  end
end

function iterFib(n)
  local f = 0
  local p1 = 0
  local p2 = 1
  for i = 0, n + 1, 1 do
    f = p1 + p2
    if i % 2 == 0 then
      p1 = p1 + p2
    else
      p2 = p2 + p1
    end
  end
  return f
end

function maxSearch()
  local nums = {}
  for i=0, 1000000, 1 do
    nums[i - 1] = math.random(0, 1000000)
  end
  local maximum = 0
  for i=0, 1000000, 1 do
    if nums[i - 1] > maximum then
      maximum = nums[i - 1]
    end
  end
  return maximum
end

function printTriangle(size)
  for i=size, 1, -1 do
    for j=1, i, 1 do
      io.write(tostring(j) .. " ")
    end
    print()
  end
end

function main()
  if(arg[1] == nil) then
    print('Usage: main.lua <n>')
    print("Choices:")
    print("[0]: hello\n[1]: fact\n[2]: sum\n[3]: recur_fib\n[4]: iter_fib\n[5]: max\n[6]: triangle\n")
    return
  end
  local n = tonumber(arg[1])
  if n < 0 or n > 6 then
    print('Invalid choice')
    return
  end
  local start = os.clock()
  if n == 0 then
    helloWorld()
  elseif n == 1 then
    print(factorial(20))
  elseif n == 2 then
    print(sum(1000000))
  elseif n == 3 then
    print(recurFib(50))
  elseif n == 4 then
    print(iterFib(50))
  elseif n == 5 then
    print(maxSearch())
  elseif n == 6 then
    printTriangle(100)
  end
  print("Time spent: " .. tostring(os.clock() - start))
end

main()
