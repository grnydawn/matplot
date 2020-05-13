"Microapp matplot module wrapper for matplotlib plotting"

import os

from typing import Any

from microapp import App


def funcargs(arg):

    if isinstance(arg, (list, tuple)):
        return arg

    else:
        return [arg], {}


class MatPlot(App):

    _name_ = "matplot"
    _version_ = "0.1.0"
    _description_ = "Microapp matplot"
    _long_description_ = "Microapp matplot"
    _author_ = "Youngsung Kim"
    _author_email_ = "youngsung.kim.act2@gmail.com"
    _url_ = "https://github.com/grnydawn/matplot"

    def __init__(self, mgr):

        self.add_argument("data", nargs="*", help="input data")

        self.add_argument("-f", metavar="newfigure",
                          help="define a figure for plotting.")
        self.add_argument("-o", "--outfile", 
                          help="file path for an image file")
        self.add_argument("--backend", type=str,
                          help="set a matplotlib backend")
        self.add_argument("-p", "--plot", metavar="plotfunc", action="append",
                          help="plot name")
        self.add_argument("--figure", metavar="figurefunc", action="append",
                          help="define Figure function.")
        self.add_argument("--axes", metavar="axesfunc", action="append",
                          help="define Axes function.")
        self.add_argument('--noshow', action='store_true',
                          help='prevent showing plot on screen.')
        self.add_argument('-t', '--title', metavar='title',
                          help='plot title')

        self.register_forward("data", type=Any, help="image data")

        self.figure = None
        self.axes = {}
        self.axes3d = None
        self.pyplots = {}
        self.plots = {}
        self._env["_pyplots_"] = self.pyplots
        self._env["_plots_"] = self.plots
        self._env["_axes_"] = self.axes

    def enter_matplot(self, mgr, args):
        pass

    def before_addplots(self, mgr, args):
        pass

    def after_addplots(self, mgr, args):
        pass

    def before_close(self, mgr, args):
        pass

    def exit_matplot(self, mgr, args):
        pass

    def perform(self, mgr, args):

        import matplotlib
        import matplotlib.pyplot as plt

        self.enter_matplot(mgr, args)

        if args.backend:
            mpl.use(args.backend["_"], warn=False, force=True)
            import matplotlib.pyplot as plt

        plots = []

        self.before_addplots(mgr, args)

        if args.plot:
            import pdb; pdb.set_trace()
            for opt in opts:

                fname = opt.get("_context_", "plot")

                if "." in fname:
                    plotfunc = eval(fname, self._env)
                    plotfunc(plotter, opt, targs)

                elif hasattr(self, fname):
                    getattr(self, fname)(plotter, opt, targs)

                elif fname in self._env:
                    self._env[fname](plotter, opt, targs)

                else:
                    targs.plot.append(opt)

        self.after_addplots(mgr, args)

        # figure setting
        if args.f:
            #self._eval(args.f)
            #vargs = args.f.vargs
            #kwargs = args.f.kwargs
            self.figure = plt.figure(*vargs, **kwargs)

        else:
            self.figure = plt.figure()

        if not self.axes:
            self.axes["ax"] = self.figure.add_subplot(111)

        if args.axes:
            pass

        elif not plots:
            if args.figure:
                pass

            elif args.data:
                for d in args.data:
                    self.axes["ax"].plot(d["_"])
            else:
                raise Exception("There is no data to plot.")

        if args.title:

            context = args.title["_context_"]
            vargs, kwargs = funcargs(args.title["_"])

            if context:
                self.axes[context].set_title(*vargs, **kwargs)
            else:
                self.axes["ax"].set_title(*vargs, **kwargs)

        if args.outfile:
            vargs, kwargs = funcargs(args.outfile["_"])
            self.figure.savefig(*vargs, **kwargs)


        self.before_close(mgr, args)

        # displyaing an image on screen
        if not args.noshow:
            plt.show()

        self.figure.clear()
        plt.close(self.figure)

        self.exit_matplot(mgr, args)


#            self.add_forward(data=f_in.read().decode())

