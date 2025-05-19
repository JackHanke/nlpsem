import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def anim(
        xs_data: list[np.array],
        loglog_data: list[np.array], 
        zipfs_data: list[np.array], 
        error_data: list[np.array],
        save_path: str = './visualizations/movie.gif', 
    ):
    
    fig, axs = plt.subplots(1, 2)

    # update function for animation
    def update(frame):
        # clear figure
        axs[0].clear()
        axs[1].clear()
        # axs[0].tick_params(labelsize=10,bottom=False,left=False,labelbottom=False,labelleft=False)
        axs[0].set_title(f'Rank Frequency Plot')
        axs[0].set_xlabel(f'Rank')
        axs[0].set_ylabel(f'Frequency')
        # axs[1].tick_params(labelsize=10,bottom=False,left=False,labelbottom=False,labelleft=False)
        axs[1].set_title(f'Zipf Error')
        axs[1].set_xlabel(f'BPE Step')
        axs[1].set_ylabel(f'Log MSE from Zipfian Prediction')

        xs = xs_data[frame]
        freqs = loglog_data[frame]
        zipf = zipfs_data[frame]

        # plot rank frequency
        axs[0].plot(
            xs, 
            freqs,
            color='green',
        )
        axs[0].plot(
            xs, 
            zipf,
            linestyle='dashed',
            color='gray',
        )
        axs[0].set_yscale(f'log')
        axs[0].set_xscale(f'log')

        # plot errors
        axs[1].plot(
            [i for i in range(frame)], 
            error_data[:frame],
            color='red',
        )
        axs[1].set_yscale(f'log')
        # axs[1].axis('off')
        axs[1].tick_params(labelleft=False)

        # Set the title based on the frame number
        fig.suptitle(f'BPE Step {frame}', fontsize=10)

        return [fig]

    # Create the animation
    anim = animation.FuncAnimation(
        fig, 
        update, 
        frames=len(loglog_data), 
        interval=1,
        blit=True
    )

    anim.save(save_path)
    print(f'Saved animation at: {save_path}')    
