function g = movingthresh(f,n,K)

f=im2double(f);
imshow(f)
[M,N]=size(f);
f(2:2:end, :)=fliplr(f(2:2:end, :));
f=f';

f=f(:)';
maf=ones(1,n)/n;
ma=filter(maf,1,f);

g=f>K*ma;

g=reshape(g,N,M)';

g(2:2:end, :)=fliplr(g(2:2:end, :));
end

