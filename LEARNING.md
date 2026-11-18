# Learning progress

## Phase 00

- Setup my local env and also my GPU
- My first lesson creating a jupyter notebook, running commands and plotting graphs on it
- I learned about python environments, created a different environment for class 06 and added some dependencies to it. The different environments can be created with uv but also with venv (native), uv is recommended because it is faster and lighweight.
- The docker setup is handful for developing and sharing what was developed with others in a easily replicated environment, that will be for sure useful in the future. I set the local container to not require a token/password because it is a local server.
- Bringing new extensions and vscode settings. I am commiting it so I can recover it from my laptop

### Lesson 09

- This lesson taught me a lot of new concepts. The new ones were Apache Arrow and Apache Parquet.
- I searched more to undestand about how those data formats works, benefits and why behind each one of them, and seeing the memory size comparison is incredible.
- Also the motivation behind the creation and also having the concern of creating something open-source aiming to support different products and vendors is something to be pride of, it helps a lot the community by having/supporting/following patterns.
- The data split itself is something great and also a must, being able to split the data and process it is great and dataset streaming is also a really useful functionality to allow many machines to work with big datasets.

### Lesson 10

- All the aliases that are provided will for sure be useful, I also added a cheat function to the aliases file to be sourced on my terminal that will allow me call cheatsheets of commands to help me get familiar with.
- I also exercised the data extraction and tmux setup.

### Lesson 11

- Basic lesson with popular commands that I'm already familiar

### Lesson 12

- I got a lot of new concepts explored on this lesson, terms like "loss", "gradients", "step size", "tensors" are more clear to me.
- Loss will be the number representing how wrong the model's prediction are right now, big number means very wrong, small means close to right
- A gradient will answer if we nudge this one weight (we have one per weight) up a bit, how much does the loss change and in which direction
- Based on the gradient, the optimizer takes each value, multiplies by the learning rate and subtracts it from the weight
- I also got an explanation about how one trainig step works:

1. Batch of data: input tensors plus the correct labels, for example shape 32, 1, 28, 28.
2. Forward pass: outputs = model(inputs). Tensors flow through layers and activations.
3. Loss: loss = criterion(outputs, labels). One number saying how wrong the predictions are.
4. Backward pass: loss.backward(). Backpropagation computes one gradient per weight.
5. Optimizer step: optimizer.step(). Each weight moves against its gradient, scaled by the learning rate.
6. Repeat: the next batch goes through the improved model, and the loss curve should trend downward. (goes back to step 2)

I ll study more about tensors and how those models behave so it is easier for me to understand the operations happening on these examples. Even though I know that it will be later explored on the course but I can't keep all those questions inside my mind

Also the most important thing is that the debugging concepts that this lesson explores are a lot helpful to be used on the day while running training sessions
