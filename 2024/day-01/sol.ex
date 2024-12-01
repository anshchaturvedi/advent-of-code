defmodule Day01 do
  defp process_input(file_name) do
    file_name
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.reduce([[], []], fn [a, b], [acc1, acc2] ->
      [[String.to_integer(a) | acc1], [String.to_integer(b) | acc2]]
    end)
  end

  def part1(file_name) do
    [arr1, arr2] = process_input(file_name)

    arr1 = Enum.sort(arr1)
    arr2 = Enum.sort(arr2)

    arr1
    |> Enum.zip(arr2)
    |> Enum.reduce(0, fn {a, b}, acc -> acc + abs(a - b) end)
  end

  def part2(file_name) do
    [arr1, arr2] = process_input(file_name)

    counter = Enum.reduce(arr2, %{}, fn num, acc ->
      count = Map.get(acc, num, 0) + 1
      Map.put(acc, num, count)
    end)

    Enum.reduce(arr1, 0, fn num, acc ->
      acc + (num * Map.get(counter, num, 0))
    end)
  end
end

IO.puts("Part 1:")
IO.puts(" " <> Integer.to_string(Day01.part1("sample.txt")))
IO.puts(" " <> Integer.to_string(Day01.part1("full.txt")))

IO.puts("Part 2:")
IO.puts(" " <> Integer.to_string(Day01.part2("sample.txt")))
IO.puts(" " <> Integer.to_string(Day01.part2("full.txt")))
