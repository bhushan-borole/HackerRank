def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    s = wrapper.fill(text=string) 
    return s