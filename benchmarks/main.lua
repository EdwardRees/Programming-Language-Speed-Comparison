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
  -- time takes: 140,737,488.355328
  -- because : 2^50 / 1000000 / 8
  if n <= 1 then
    return 1
  else
    if n % 10 == 0 then
      count = count + 1
      if(count % 1000000 == 0) then
        print(count / 1000000)
      end
    end
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
  local start = os.clock()
  print(printTriangle(100))
  print(os.clock() - start)
end

main()