$result_hash = {}

def fibo_use_cache(num)
  puts "fibo(#{num})"
  if num == 0
    return 0
  elsif num == 1
    return 1
  end

  if $result_hash.has_key?(num)
    return $result_hash[num]
  end
  result = fibo_use_cache(num-1) + fibo_use_cache(num-2)
  $result_hash[num] = result
  return result
end

# def fibo(num)
#   puts "fibo(#{num})"
#   if num == 0
#     return 0
#   elsif num == 1
#     return 1
#   end

#   result = fibo(num-1) + fibo(num-2)
#   return result
# end

def main()
  input = 6
  # puts fibo(input)
  puts "[Result] #{fibo_use_cache(input)}"
end

main()
