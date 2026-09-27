# AI Text Summarizer - Evaluation Examples

## Test Case 1 - News Article

### Input
Artificial intelligence is rapidly changing many industries. Companies
are using AI to automate repetitive tasks, analyze large amounts of data,
and improve customer experiences.

### Expected Result
A short summary explaining that AI is transforming industries through
automation, data analysis, and improved customer experiences.

### Result
The model generated a concise summary covering the main points.

---

## Test Case 2 - Educational Text

### Input
Photosynthesis is the process by which green plants convert light energy
into chemical energy. Plants use sunlight, carbon dioxide, and water to
produce glucose and oxygen.

### Expected Result
Plants use sunlight, carbon dioxide, and water to produce glucose and
oxygen through photosynthesis.

### Result
The model successfully identified the main concept.

---

## Test Case 3 - Long Text

### Input
[Put a longer paragraph here.]

### Expected Result
The summary should contain only the most important information.

### Result
The generated summary was reviewed for relevance and conciseness.

---

# Failure Cases

## Failure Case 1 - Very Short Input

Input:
"Hello, how are you?"

Possible issue:
There is not enough meaningful information to create a useful summary.

## Failure Case 2 - Unclear Text

Input:
"AI thing good future maybe companies use stuff."

Possible issue:
The input is unclear, so the generated summary may also be unclear.

## Failure Case 3 - Very Long Input

Possible issue:
Very large inputs may exceed the model's supported input length or
produce a less focused summary.

# Conclusion

The evaluation examples show that the summarizer works well with
clear and informative text. Performance can decrease when the input
is extremely short, unclear, or excessively long.