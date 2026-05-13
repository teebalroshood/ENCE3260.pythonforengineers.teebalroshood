# Lab_6

# Counting Chocolates with Computer Vision

## Conceptual Questions

### 1. How do the chocolates differ from the background in terms of pixel intensity?

The chocolates are darker than the background in the grayscale image. This means the chocolates have lower pixel intensity values than the background.

---

### 2. If you apply a threshold to the grayscale image, what threshold value separates the chocolates from the background? How did you determine it?

A threshold value around 100 worked well for separating the chocolates from the background. This value was chosen by testing different values and selecting the one that best highlighted the chocolates while reducing noise.

---

### 3. How can you use the expected size of a chocolate to your advantage?

Since the chocolates are about the same size, very small detected regions can be ignored because they are likely noise instead of chocolates.

---

### 4. What happens if two chocolates are close together — how might that affect your count?

If two chocolates are touching or very close together, they may be detected as one object instead of two separate chocolates. This can make the count lower than the actual number.

---

### 5. What does it mean for the pixels inside a candidate region to be "uniform"? Why is uniformity a useful property to check?

Uniformity means the pixels inside a region look similar in brightness or appearance. This is useful because real chocolates usually have consistent shading, while noise and unwanted regions do not.
