find -E -L . -not -path "./trash/*" -regex ".*\.(aux|auxlock|bbl|blg|dvi|tmp|out|fdb_latexmk|fls|ilg|ind|tdo|toc|bcf|run\.xml)" | while read file
do 
  dir=$(dirname $file)
  echo "$file to trash/$dir"
  mkdir -p trash/$dir
  mv $file trash/$dir
done

echo "Removing externalized Tikz figures..."
find -E tikzfigures/ -type f -not -name "README.md" | while read file
do
  rm $file
done

if [ -f "main.makefile" ]
then
  rm main.makefile
fi

