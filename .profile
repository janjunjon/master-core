# ~/.profile: executed by Bourne-compatible login shells.

if [ "$BASH" ]; then
  if [ -f ~/.bashrc ]; then
    . ~/.bashrc
  fi
fi

mesg n 2> /dev/null || true

export Tutorial_DIR=$HOME/scale-5.4.4/scale-rm/test/tutorial
export SCALE_DB=$HOME/scale-5.4.4/scale_database
