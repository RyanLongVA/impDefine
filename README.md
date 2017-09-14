# impDefine
Status: Basic Completition; finished

## Usage
`python impDefine.py -i <input link list> -s "<string to look for>" *optional* -s "<second string>"`
Note: if you want to include quotes like for json output, the shell escapes those unless you do \" \" or enclose them in singles -->  '""'

I run into a absolute ton of domains that are identical in some fashion during recon (e.g. Blank Page, Repeated Errors, etc.) the point is just hacking up something that searches the entire output for the exact strings you define and spits out the urls/responses thatdon't include what you provided 
