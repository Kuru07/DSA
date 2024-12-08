//To find an min and max element of an array

/*
class Pair<K, V> {
    private final K key;
    private final V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() {
        return key;
    }

    public V getValue() {
        return value;
    }
}

Java users need to return result in Pair class
For Example -> return new Pair(minimum,maximum)
*/

class Solution {
    public Pair<Long, Long> getMinMax(int[] arr) {
        int n=arr.length-1;
        Arrays.sort(arr);
        return new Pair(arr[0],arr[n]);
    }
}