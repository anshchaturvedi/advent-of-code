defmodule Day02 do
  defp process_input(file_name) do
    file_name
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.map(fn a -> Enum.map(a, &String.to_integer/1) end)
  end

  defp is_report_safe?(report) do
    chunked = Enum.chunk_every(report, 2, 1, :discard)

    is_report_monotonic?(chunked, :increasing) or is_report_monotonic?(chunked, :decreasing)
  end

  def is_report_monotonic?(chunked_report, :increasing) do
    Enum.all?(chunked_report, fn [a, b] -> a < b and b - a <= 3 end)
  end

  def is_report_monotonic?(chunked_report, :decreasing) do
    Enum.all?(chunked_report, fn [a, b] -> a > b and a - b <= 3 end)
  end

  def part1(file_name) do
    file_name
    |> process_input()
    |> Enum.reduce(0, fn report, acc ->
      acc + if is_report_safe?(report), do: 1, else: 0
    end)
  end

  def part2(file_name) do
    file_name
    |> process_input()
    |> Enum.reduce(0, fn report, acc ->
      possible_reports = Enum.map(0..(length(report) - 1), &List.delete_at(report, &1))

      if Enum.any?([report | possible_reports], &is_report_safe?/1) do
        acc + 1
      else
        acc
      end
    end)
  end
end

IO.puts("Part 1:")
IO.puts(" " <> Integer.to_string(Day02.part1("sample.txt")))
IO.puts(" " <> Integer.to_string(Day02.part1("full.txt")))

IO.puts("Part 2:")
IO.puts(" " <> Integer.to_string(Day02.part2("sample.txt")))
IO.puts(" " <> Integer.to_string(Day02.part2("full.txt")))
