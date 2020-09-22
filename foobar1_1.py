def solution(text):
  sequence = []
  max_len = 0
  end = 0
  longest = ''

  for i in range(len(text)):
    current_sequence = ''.join(sequence)
    if current_sequence:
        temp_list = text.split(current_sequence)
        if len(''.join(temp_list)) == 0 and text.count(current_sequence) > max_len:
          longest = current_sequence
          max_len = len(current_sequence)

    sequence.append(text[end])
    end = end + 1

  num_slices = text.count(longest)

  return num_slices
