# Run routine

Run your routines by passing it's reference and array of arguments

Important note: this is **NOT A REAL ALGORITHM**! This has been made, works and will work only in the game called Grey Hack!




## Table of contents

1.  [What's this?](#what-is-this)
2.  [License](#license)
3.  [Thanks and Credits](#thanks-and-credits)




## What's even this??? <a name="what-is-this"></a>

Basically it's a mess of if-checks that allows you to run your function without invoking it directly. Still don't get it? Well, here are the example:

Let's say we have a function:

```javascript
add = function(a, b)
    return a + b
end function
```

So that's how we invoke it directly:

```javascript
print(add(2, 3)) // 5
```

But with this "algorithm" you can go crazy and do this instead:

```javascript
print(run(@add, [2, 3])) // 5
```

Why would you ever need this, you may ask? The answer is **I don't know**. That's just what I thought would be cool to have just in case, but for now, I see no real use cases for this :P




## License <a name="license"></a>

In case this even should be licensed, Run routine is licensed under MIT No Attribution. See [here](LICENSE) for full details




## Thanks and Credits <a name="thanks-and-credits"></a>

Special thanks and credits goes to:

-   [Kurouzu](https://steamcommunity.com/profiles/76561198135838638) - for [Grey Hack](https://store.steampowered.com/app/605230/Grey_Hack/)
-   [Joe Strout](https://github.com/JoeStrout) - for [MiniScript](https://github.com/JoeStrout/miniscript)
