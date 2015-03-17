find -E . -follow -not -path "./trash/*" -regex ".*\.(aux|bbl|blg|dvi|tmp|out|fdb_latexmk|fls|ilg|ind|tdo|toc|bcf|run\.xml)" | while read file
do 
  dir=$(dirname $file)
  echo "$file to trash/$dir"
  mkdir -p trash/$dir
  mv $file trash/$dir
done

