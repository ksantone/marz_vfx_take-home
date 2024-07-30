import React, { useEffect, useState } from 'react';
import ProductItem from '../../components/ProductItem/ProductItem';
import { Product } from '../../components/interfaces';
import PageWrapper from '../PageWrapper';

const ProductsPage = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchProducts = async () => {
    try {
      const response = await fetch('/api/products');
      const data = await response.json();
      setProducts(data.filter((product: Product) => product.ProductStatus === 'Active'));
    } catch (error) {
      console.error('Error fetching products:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  if (loading) {
    return <div className="text-center text-white">Loading...</div>;
  }

  return (
    <PageWrapper>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {products.map((product) => (
          <ProductItem key={product.ProductID} product={product} />
        ))}
      </div>
    </PageWrapper>
  );
};

export default ProductsPage;