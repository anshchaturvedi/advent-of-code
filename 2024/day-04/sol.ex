defmodule Day03 do
  defp process_input(file_name) do
    file_name
    |> File.read!()
    |> String.split("\n", trim: true)
  end

  defp graph_to_map(graph, rows, cols) do
    0..(rows - 1)
    |> Enum.reduce(%{}, fn i, acc1 ->
      0..(cols - 1)
      |> Enum.reduce(%{}, fn j, acc2 ->
        Map.put(acc2, {i, j}, graph |> Enum.at(i) |> String.at(j))
      end)
      |> Map.merge(acc1)
    end)
  end

  def part1(file_name) do
    graph = file_name |> process_input()
    {rows, cols} = {length(graph), graph |> List.first() |> String.length()}
    graph = graph_to_map(graph, rows, cols)

    for i <- 0..(rows - 1), j <- 0..(cols - 1) do
      if Map.get(graph, {i, j}) == "X" do
        up = Enum.map(i..(i - 3), fn x -> Map.get(graph, {x, j}, "") end) |> Enum.join("")
        down = Enum.map(i..(i + 3), fn x -> Map.get(graph, {x, j}, "") end) |> Enum.join("")
        left = Enum.map(j..(j - 3), fn x -> Map.get(graph, {i, x}, "") end) |> Enum.join("")
        right = Enum.map(j..(j + 3), fn x -> Map.get(graph, {i, x}, "") end) |> Enum.join("")

        up_right = Enum.map(0..3, fn d -> Map.get(graph, {i - d, j + d}, "") end) |> Enum.join("")
        up_left = Enum.map(0..3, fn d -> Map.get(graph, {i - d, j - d}, "") end) |> Enum.join("")

        down_right =
          Enum.map(0..3, fn d -> Map.get(graph, {i + d, j + d}, "") end) |> Enum.join("")

        down_left =
          Enum.map(0..3, fn d -> Map.get(graph, {i + d, j - d}, "") end) |> Enum.join("")

        all_possible = [up, down, left, right, up_right, up_left, down_right, down_left]
        Enum.count(all_possible, &(&1 == "XMAS"))
      end
    end
    |> Enum.filter(&(not is_nil(&1)))
    |> Enum.sum()
  end

  def part2(file_name) do
    graph = file_name |> process_input()
    {rows, cols} = {length(graph), graph |> List.first() |> String.length()}
    graph = graph_to_map(graph, rows, cols)
    valid = ["MAS", "SAM"]

    for i <- 0..(rows - 1), j <- 0..(cols - 1) do
      if Map.get(graph, {i, j}) == "A" do
        pos_diagonal =
          Enum.map(-1..1, fn d -> Map.get(graph, {i - d, j + d}) end) |> Enum.join("")

        neg_diagonal =
          Enum.map(-1..1, fn d -> Map.get(graph, {i + d, j + d}) end) |> Enum.join("")

        if Enum.member?(valid, pos_diagonal) and Enum.member?(valid, neg_diagonal), do: 1
      end
    end
    |> Enum.filter(&(not is_nil(&1)))
    |> Enum.sum()
  end
end

IO.puts("Part 1:")
IO.puts(" " <> Integer.to_string(Day03.part1("sample.txt")))
IO.puts(" " <> Integer.to_string(Day03.part1("full.txt")))

IO.puts("Part 2:")
IO.puts(" " <> Integer.to_string(Day03.part2("sample.txt")))
IO.puts(" " <> Integer.to_string(Day03.part2("full.txt")))
