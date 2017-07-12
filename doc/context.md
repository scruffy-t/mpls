## context files

The plotting context, or simply *context*, is a parameter dict that controls the **size** of figure elements, such as the `figsize`, `font.size`, and so on.

> Technically, the *context* dict represents a small part of the `rcParams` dict in [matplotlib][1]. Please, refer to the [respective matplotlib page][2] for more information on how to customize the style of your plots directly in matplotlib.

[seaborn][3] provides four base context parameter sets, namely *notebook*, *paper*, *talk*, and *poster*. The three latter are versions of the *notebook* parameters scaled by 0.8, 1.3, and 1.6, respectively.

```javascript
{
	// [height, width] of the figure in inches
	// 1 inch == 2.54 cm
	"figure.figsize": [4, 3],

	// font sizes, all in units of pt
	"font.size": 10,
	"axes.labelsize": 10,
	"axes.titlesize": 10,
	"xtick.labelsize": 8,
	"ytick.labelsize": 8,
	"legend.fontsize": 10,

	"grid.linewidth": 0.5,
	"lines.linewidth": 1,
	"patch.linewidth": 1,
	"lines.markersize": 2,
	"lines.markeredgewidth": 1,

	"xtick.major.width": 1,
	"ytick.major.width": 1,
	"xtick.minor.width": 1,
	"ytick.minor.width": 1,

	"xtick.major.pad": 1,
	"ytick.major.pad": 1
}
```

[1]: http://matplotlib.org
[2]: http://matplotlib.org/users/customizing.html
[3]: http://seaborn.pydata.org
