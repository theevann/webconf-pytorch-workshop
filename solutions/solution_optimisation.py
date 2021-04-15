y = f(x)
loss = y.abs()
loss.backward()
with torch.no_grad():
    x -= lr * x.grad
    x.grad.zero_()

y = f(x)
loss = loss_function(y, y_target)
loss.backward()
optimizer.step()
optimizer.zero_grad()
